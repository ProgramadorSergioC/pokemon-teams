import { useLocation, Navigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { logOut } from "./AuthSlice";

const Logout = () => {
  const dispatch = useDispatch();
  dispatch(logOut());
  const location = useLocation();
  return <Navigate to="/" state={{ from: location }} replace />;
};

export default Logout;
