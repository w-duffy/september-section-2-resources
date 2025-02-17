import {
  createBrowserRouter,
} from "react-router-dom";
import LoginFormPage from "../components/LoginFormPage";
import SignupFormPage from "../components/SignupFormPage";
import Layout from "./Layout";
import AWS, {Images} from "../components/AWS";
import ImageDetail from "../components/ImageDetail";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <AWS />,
      },
      {
        path: "image/:id",
        element: <ImageDetail />
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "images",
        loader: async () => fetch("/api/images"),
        element: <Images />,
      },
    ],
  },
]);
