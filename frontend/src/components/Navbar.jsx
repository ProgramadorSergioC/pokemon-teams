// Navbar.jsx
import React from "react";
import { useState } from "react";
import { Outlet } from "react-router-dom";
import LoginPopup from "./LoginPopup";
import { logOut } from "../features/auth/AuthSlice";
import { useSelector } from "react-redux";
import { Button } from "react-bootstrap";

const Navbar = () => {
  const [isPopupOpen, setIsPopupOpen] = useState(false);

  const openPopup = () => {
    setIsPopupOpen(true);
  };

  const closePopup = () => {
    setIsPopupOpen(false);
  };

  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

  return (
    <>
      {/* <div className="container mx-auto ml-20 mr-10"> */}
      <nav className="bg-white p-3 rounded-lg shadow-lg my-4 w-full">
        <div className="flex justify-between">
          <NavLink to="/">Home</NavLink>
          <NavLink to="/pokedex">Pokedex</NavLink>
          <NavLink to="/">Boxes</NavLink>
          <NavLink to="/">Teams</NavLink>
          <NavLink to="/">Combat</NavLink>

          {isAuthenticated ? (
            <NavLink to="/logout">Logout</NavLink>
          ) : (
            <a
              className="text-black text-lg font-semibold p-2 transition duration-300 hover:text-red-500 hover:border-gray-300 border-b hover:border-red-500"
              onClick={openPopup}
            >
              Sign In
            </a>
          )}
          <LoginPopup isOpen={isPopupOpen} onClose={closePopup} />
        </div>
      </nav>
      {/* </div> */}
      <Outlet />
    </>
  );
};

const NavLink = ({ to, children }) => {
  return (
    <a
      href={to}
      className="text-black text-lg font-semibold p-2 transition duration-300 hover:text-red-500 hover:border-gray-300 border-b hover:border-red-500"
    >
      {children}
    </a>
  );
};

export default Navbar;
