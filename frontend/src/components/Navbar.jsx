// Navbar.jsx
import React from "react";
import { useState } from "react";
import { Outlet } from "react-router-dom";
import LoginPopup from "./LoginPopup";
import { useDispatch, useSelector } from "react-redux";

const Navbar = () => {
  const [isPopupOpen, setIsPopupOpen] = useState(false);

  const openPopup = () => {
    setIsPopupOpen(true);
  };

  const closePopup = () => {
    setIsPopupOpen(false);
  };

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
          <button
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
            onClick={openPopup}
          >
            Iniciar Sesión
          </button>

          {isPopupOpen && <LoginPopup onClose={closePopup} />}
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
