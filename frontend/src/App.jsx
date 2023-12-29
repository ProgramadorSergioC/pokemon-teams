import { Routes, Route } from "react-router-dom";
import "./App.css";
import Navbar from "./components/Navbar";
import Pokedex from "./routes/pokedex";
import Home from "./routes/home";
import Login from "./features/auth/Login";
import RequireAuth from "./features/auth/RequireAuth";

function App() {
  return (
    <div className="container mx-auto w-70">
      <Routes>
        <Route path="/" element={<Navbar />}>
          {/* public routes */}
          <Route index element={<Home />} />
          <Route path="/login" element={<Login />} />
          {/* protected routes */}
          <Route element={<RequireAuth />}>
            <Route path="/pokedex" element={<Pokedex />} />
          </Route>
        </Route>
      </Routes>
    </div>
  );
}

export default App;
