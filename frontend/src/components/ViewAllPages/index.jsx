import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { NavLink } from 'react-router-dom';
import { Button } from '@mui/material';
import { css } from '@emotion/react';
import { useEmployees } from "../../contexts/EmployeesContext.js";
import EmployeeCard from './EmployeeCard.jsx';
import RoleCard from './RoleCard.jsx';
import './index.css';

function ViewAllPages({ formType, items }) {

    const navigate = useNavigate();

    const date = new Date();

    const handleEmployeesBtn = (e) => {
        e.preventDefault();
        return navigate("/employees/all");
    }

    const handleCreateNewEmployee = (e) => {
        e.preventDefault();
        return navigate("/employees/new");
    }

    const handleCreateNewRole = (e) => {
        e.preventDefault();
        return navigate("/roles/new");
    }

    const handleRolesBtn = (e) => {
        e.preventDefault();
        return navigate("/roles/all");
    }


    return (
        <div className='view-all-container'>
            <div
                className='view-all-nav'
            >
                <Button
                    disabled={formType === "Employees" ? true : false}
                    onClick={handleEmployeesBtn}
                >
                    Employees
                </Button>
                |
                <Button
                    disabled={formType === "Roles" ? true : false}
                    onClick={handleRolesBtn}
                >
                    Roles
                </Button>
            </div>
            <div
                className='view-all-header'
            >
                <h1>
                    View All {formType}
                </h1>
            </div>
            <Button
                onClick={formType ==="Employees" ? handleCreateNewEmployee : handleCreateNewRole }
            >
                +   Create New { formType === "Employees" ? "Employee" : "Role" }
            </Button>
            <ul className='view-all-items'>
                <li
                    id='view-all-table-header'
                    key='view-all-table-header'
                >
                    <div className='view-all-items-header'>
                        {
                            formType === 'Employees' ? (
                                <>
                                
                                    <div className='employee-card-last-name'>
                                        <p>
                                            Last Name
                                        </p>
                                    </div>
                                    <div className='employee-card-first-name'>
                                        <p>
                                            First Name
                                        </p>
                                    </div>
                                    <div className='employee-card-employee-id'>
                                        <p>
                                            Employee ID
                                        </p>
                                    </div>
                                    <div className='employee-card-food-permit'>
                                        <p>
                                            Food Permit Expiration
                                        </p>
                                    </div>
                                    <div className='employee-card-alcohol-permit'>
                                        <p>
                                            Alcohol Permit Expiration
                                        </p>
                                    </div>
                                    <div className='employee-card-action'>
                                        <p>
                                            Action
                                        </p>
                                    </div>
                                </>
                            ) : (
                                <>
                                    <div className='role-card-role'>
                                        <p>
                                            Role Name
                                        </p>
                                    </div>
                                    <div className='role-card-action'>
                                        <p>
                                            Actions
                                        </p>
                                    </div>
                                </>
                            )
                        }
                    </div>
                </li>
                {
                    items.map(i => {
                        if (formType === "Employees") return (<EmployeeCard employee={i} date={date} />);
                        if (formType === "Roles") return (<RoleCard role={i} />)
                    })
                }
            </ul>
        </div>
    );

}

export default ViewAllPages;
