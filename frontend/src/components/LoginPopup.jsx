import React, { useState } from "react";
import LoginForm from "./LoginForm";

const LoginPopup = ({ onClose }) => {
  return (
    <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-800 bg-opacity-50">
      <div className="bg-white p-8 rounded-lg shadow-md w-96">
        <button onClick={onClose}>
          <i class="fa-solid fa-xmark"></i>
        </button>
        <h2 className="text-2xl font-bold mb-4">Iniciar Sesión</h2>
        <LoginForm onClose={onClose} />
      </div>
    </div>
  );
};

export default LoginPopup;
