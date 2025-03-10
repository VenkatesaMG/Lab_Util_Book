import { Router } from "express";
import {
  getNotifications,
  createNotification,
  markAsRead,
  markAllAsRead,
  deleteNotification,
  deleteAllNotifications, 
} from "../Controllers/Notification_Controller.js";

const router = Router();

router.get("/notifications", getNotifications);
router.post("/notifications", createNotification);
router.patch("/notifications/:id", markAsRead);
router.patch("/notifications",markAllAsRead);
router.delete("/notifications/:id", deleteNotification); 
router.delete("/notifications", deleteAllNotifications);

export default router;