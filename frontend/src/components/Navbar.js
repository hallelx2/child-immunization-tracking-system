import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/profile">Profile</Link></li>
                <li><Link to="/immunizations">Immunizations</Link></li>
                <li><Link to="/milestones">Milestones</Link></li>
                <li><Link to="/schedules">Schedules</Link></li>
                <li><Link to="/reports">Reports</Link></li>
            </ul>
        </nav>
    );
};

export default Navbar;
