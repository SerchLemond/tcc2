import ChatPage from "@/modules/chat";
import DashboardPage from "@/modules/dashboard";
import { createBrowserRouter } from "react-router-dom";

export const router = createBrowserRouter([
  { path: "/", element: <ChatPage /> },
  { path: "/dashboard", element: <DashboardPage /> },
]);
