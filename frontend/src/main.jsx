import { createRoot } from "react-dom/client";
import "./globals.css";
import { RouterProvider } from "react-router-dom";
import { router } from "./routes/routes";
import { Toaster } from "./components/ui/toaster";
createRoot(document.getElementById("root")).render(<>
      <RouterProvider router={router}/>
      <Toaster /> 
  </>);
