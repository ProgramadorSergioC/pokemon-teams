// LoginModal.jsx
import React, { useState } from "react";
import { useHistory } from "react-router-dom"; // Asume que estás utilizando react-router-dom

const LoginModal = ({ isOpen, onClose, onLogin }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const history = useHistory();

  const handleLogin = () => {
    // Realizar lógica de inicio de sesión aquí
    // Luego, cerrar el modal y redirigir al usuario
    onLogin();

    // Redirigir a la URL después del inicio de sesión
    const redirectUrl = sessionStorage.getItem("redirectUrl") || "/";
    history.push(redirectUrl);

    onClose();
  };

  return (
    <div className={`modal ${isOpen ? "visible" : "hidden"}`}>
      <div className="modal-content">
        {/* Contenido del formulario de inicio de sesión */}
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={handleLogin}>Iniciar sesión</button>
      </div>
    </div>
  );
};

export default LoginModal;
