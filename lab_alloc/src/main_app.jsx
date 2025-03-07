import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import App from "./App.jsx";
import AdminInterface from "./components/AdminInterface.jsx";
import ResourceAllocationInterface from "./components/Resource_Allocation_Interface.jsx";
import Scanner from "./components/scanner.jsx";
import CancelLab from "./components/CancelLab.jsx";
import BookLabForm from "./components/comp_v/BookLabForms.jsx";
import { useState } from "react";
import ResourceAllocation from "./components/Resource_allocation.jsx";
import AdminResourceAllocation from "./components/AdminResourceAllocation.jsx";
import ScheduleMain from "./components/comp_v/ScheduleMain.jsx";
function MainApp() {
  const [pageState, setPageState] = useState("Dashboard");
  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={<App pageState={pageState} setPageState={setPageState} />}
        />
        <Route path="/temp" element={<ScheduleMain />} />
        <Route
          path="/book"
          element={<BookLabForm setPageState={setPageState} />}
        />
        <Route
          path="/resource"
          element={<ResourceAllocationInterface></ResourceAllocationInterface>}
        />
        <Route
          path="/admin_resource"
          element={<AdminResourceAllocation></AdminResourceAllocation>}
        />
        <Route path="/resourcealloc" element={<ResourceAllocation />} />
        <Route path="/scan" element={<Scanner />} />
        <Route path="/cancel-lab" element={<CancelLab />} />
        <Route path="/admin" element={<AdminInterface></AdminInterface>} />
        {/* <Route path='/login' element={<Login />} /> */}
      </Routes>
    </Router>
  );
}

export default MainApp;
