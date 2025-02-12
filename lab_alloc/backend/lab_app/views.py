from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from lab_app.models import Schedules, User, Laboratory
from rest_framework import generics
from lab_app.serializers import ScheduleSerializer, LaboratorySerializer, UserSerializer
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, datetime

class ScheduleProcessor:
    def __init__(self):
        self.day = dict()
        self.cur_date = datetime.now().date()
        self.ordered = dict()

    def process_labs(self):
        cur_time = datetime.now().time()
        labs = Schedules.objects.filter(schedule_date=self.cur_date, schedule_from__gt=cur_time).order_by("schedule_from")

        for lab in labs:
            if lab.lab_id_id not in self.day:
                self.day[lab.lab_id_id] = [[(lab.schedule_from, lab.schedule_to)]]
                self.ordered[lab.lab_id_id] = [(lab.schedule_from, lab.schedule_to)]
            else:
                flag = True
                for session in self.day[lab.lab_id_id]:
                    if lab.schedule_from >= session[-1][1]:
                        session.append((lab.schedule_from, lab.schedule_to))
                        self.ordered[lab.lab_id_id].append((lab.schedule_from, lab.schedule_to))
                        flag = False
                        break

                if flag:
                    self.day[lab.lab_id_id].append([(lab.schedule_from, lab.schedule_to)])
                    self.ordered[lab.lab_id_id].append((lab.schedule_from, lab.schedule_to))


    def add_session(self, new_session, lab_id):
        print("Inside add_session")
        cur_time = datetime.now().time()
        updated_levels = []
        capacity = Laboratory.objects.get(lab_id=lab_id).lab_capacity
        print("Capacity:", capacity)

        if lab_id not in self.ordered:
            self.ordered[lab_id] = []

        self.ordered[lab_id] = [session for session in self.ordered[lab_id] if session[0] >= cur_time]

        self.ordered[lab_id].append(new_session)
        self.ordered[lab_id].sort(key = lambda x : x[0])

        for session in self.ordered[lab_id]:
            if not updated_levels:
                updated_levels.append([session])
            else:
                flag = False
                for index, level in enumerate(updated_levels):
                    if session[0] >= level[-1][1]:
                        if len(updated_levels) >= capacity:
                            self.ordered[lab_id] = []
                            self.process_labs()
                            return False

                        updated_levels[index].append(session)
                        flag = True
                        break

                if not flag:
                    updated_levels.append([session])
        self.day[lab_id] = updated_levels
        return True


schedule_processor = ScheduleProcessor()
schedule_processor.process_labs()

class ScheduleCreateAPIView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['lab_id'] = Laboratory.objects.get(lab_name = data['lab_name']).lab_id
        data.pop('lab_name')

        serializer = ScheduleSerializer(data=data)
        if(serializer.is_valid()):
            schedule_from = serializer.validated_data['schedule_from']
            schedule_to = serializer.validated_data['schedule_to']
            lab_id = serializer.validated_data['lab_id'].lab_id
            if schedule_processor.add_session((schedule_from, schedule_to), lab_id):
                serializer.save()
                return Response({"Message": "Successfully created a session"})
            else:
                return Response({"Message" : "Cannot create a session"})

schedule_create_view = ScheduleCreateAPIView.as_view()

class ScheduleListAPIView(generics.ListAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

schedule_list_view = ScheduleListAPIView.as_view() 

class ScheduleListDetailAPIView(generics.ListAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        lab_name = self.kwargs.get('lab_name')
        date_str = self.kwargs.get('date')

        try:
            lab_id = Laboratory.objects.get(lab_name=lab_name).lab_id
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except Exception as e:
            print("Error : ",e)
            return Schedules.objects.none()
        try:
            queryset = self.queryset.filter(lab_id = lab_id)
            queryset = queryset.filter(schedule_date = date)
            return queryset
        except Exception as e:
            print("Error while fetching from Schedule : ",e)
            return Schedules.objects.none()

schedule_list_detail_view = ScheduleListDetailAPIView.as_view()

class LaboratoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

laboratory_list_create_view = LaboratoryListCreateAPIView.as_view()

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

user_list_create_view = UserListCreateAPIView.as_view()

class LaboratoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer
    lookup_field = 'lab_id'

    def perform_update(self, serializer):
        instance = serializer.save()