import { Routes, Route } from "react-router-dom";
import "./App.css";
import Navbar from "./components/Navbar";
import Pokedex from "./features/pokemons/pokedex";
import Home from "./features/home";
import Login from "./features/auth/Login";
import RequireAuth from "./features/auth/RequireAuth";
import Logout from "./features/auth/Logout";

function App() {
  return (
    <div className="container mx-auto w-70">
      <Routes>
        <Route path="/" element={<Navbar />}>
          {/* public routes */}
          <Route index element={<Home />} />
          <Route path="/logout" element={<Logout />} />
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
