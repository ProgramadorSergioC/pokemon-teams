import { useLocation, Navigate, Outlet } from "react-router-dom";
import { useSelector } from "react-redux";
import {
  selectCurrentToken,
  selectCurrentRefresh,
  selectCurrentUser,
  setTokenCredentials,
} from "./AuthSlice";
import { logOut } from "./AuthSlice";
import { useRefreshMutation } from "./AuthApiSlice";
import { useDispatch } from "react-redux";
import { useEffect } from "react";

const decodeJWT = (token) => {
  try {
    return JSON.parse(atob(token.split(".")[1]));
  } catch (e) {
    return null;
  }
};

const isTokenExpired = (token) => {
  try {
    const decoded = decodeJWT(token);
    if (!decoded || !decoded.exp) {
      // Invalid or expirated token
      return true;
    }
    const currentTime = Math.floor(Date.now() / 1000); // en segundos
    return currentTime > decoded.exp;
  } catch (error) {
    return true;
  }
};

const RefreshTokenHandler = () => {
  const [refresh, { isLoading }] = useRefreshMutation();
  const dispatch = useDispatch();
  const refreshToken = useSelector(selectCurrentRefresh);
  const username = useSelector(selectCurrentUser);

  useEffect(() => {
    const userefreshToken = async () => {
      try {
        const userData = await refresh(refreshToken).unwrap();
        dispatch(setTokenCredentials({ ...userData, username }));
        console.log("Refresh token");
      } catch (err) {
        logOut();
      }
    };

    userefreshToken();
  }, [dispatch, refreshToken, refresh, username]);

  return null;
};

const RequireAuth = () => {
  let token = useSelector(selectCurrentToken);
  const location = useLocation();
  if (token) {
    if (isTokenExpired(token)) {
      console.log("Token expired");
      return <RefreshTokenHandler />;
    }
  }

  return token ? (
    <Outlet />
  ) : (
    <Navigate to="/login" state={{ from: location }} replace />
  );
};
export default RequireAuth;
