import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import NavBar from './components/NavBar';
import Dashboard from './components/Dashboard';
import Employee from './components/Employees/index.jsx';
import EmployeeForm from './components/EmployeeForm/index.jsx';
import { useAuth } from './contexts/AuthenticationContext';
import { theme } from './contexts/ThemeContext';

export default function App() {
    const { isAuthenticated } = useAuth();
    const [mode, setMode] = useState(theme);
    const toggleTheme = () => {
        setMode(prevState => !prevState);
    }
    return (
        <>
            {isAuthenticated && <NavBar toggleTheme={toggleTheme} />}
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route exact path="/dashboard" element={<Dashboard />} />
                <Route exact path="/employees" element={<Employee />} />
            </Routes>
        </>
    );
}