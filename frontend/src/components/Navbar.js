import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">CONTENTIQ</div>
      <div className="nav-links">
        <Link to="/">HOME</Link>
        <Link to="/analyze">ANALYZE</Link>
        <Link to="/about">ABOUT</Link>
      </div>
    </nav>
  );
}

export default Navbar;