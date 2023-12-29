// LoginPopup.jsx
import React, { useRef, useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { setCredentials } from "../features/auth/AuthSlice";
import { useLoginMutation } from "../features/auth/AuthApiSlice";
import { useNavigate, useLocation } from "react-router-dom";
import LoginForm from "./LoginForm";
import { Modal, Button, Form } from "react-bootstrap";

const LoginPopup = ({ isOpen, onClose }) => {
  const userRef = useRef();
  const errRef = useRef();
  const [username, setUser] = useState("");
  const [password, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const navigate = useNavigate();
  const location = useLocation();

  const [login, { isLoading }] = useLoginMutation();
  const dispatch = useDispatch();

  useEffect(() => {
    if (isOpen && userRef.current) {
      userRef.current.focus();
    }
  }, [isOpen]);

  useEffect(() => {
    setErrMsg("");
  }, [username, password]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const userData = await login({ username, password }).unwrap();
      dispatch(setCredentials({ ...userData, username }));
      localStorage.setItem("token", userData.access);
      localStorage.setItem("refresh", userData.refresh);
      localStorage.setItem("user", userData.username);
      setUser("");
      setPwd("");
      onClose(); // Cerrar el modal después del inicio de sesión
      navigate(location.pathname); // Redirigir al usuario
    } catch (err) {
      // Resto del código permanece igual
    }
  };

  const handleUserInput = (e) => setUser(e.target.value);

  const handlePwdInput = (e) => setPwd(e.target.value);

  return (
    <Modal show={isOpen} onHide={onClose}>
      <Modal.Header closeButton>
        <Modal.Title>Iniciar sesión</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form>
          <Form.Group controlId="formUsername">
            <Form.Label>Username</Form.Label>
            <Form.Control
              type="username"
              placeholder="Username"
              value={username}
              onChange={handleUserInput}
              required
            />
          </Form.Group>

          <Form.Group controlId="formPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Password"
              value={password}
              onChange={handlePwdInput}
              required
            />
          </Form.Group>

          <Button variant="primary" onClick={handleSubmit}>
            Sign In
          </Button>
        </Form>
      </Modal.Body>
    </Modal>
  );
};

export default LoginPopup;
