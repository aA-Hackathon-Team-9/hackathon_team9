import React, { useEffect, useState } from 'react';
import './index.css';

export default function EmployeeForm({ employee, formType }) {

    const [firstName, setFirstName] = useState(employee.firstName);
    const [lastName, setLastName] = useState(employee.lastName);
    const [restaurantId, setRestaurantId] = useState(employee.restaurantId);
    const [role, setRole] = useState([[...employee.role]]);
    const [foodPermitExp, setFoodPermitExp] = useState(employee.foodPermitExp);
    const [alcoholPermitExp, setAlcoholPermitExp] = useState(employee.alcoholPermitExp);

    const [validationErrors, setValidationErrors] = useState({
        firstName: '',
        lastName: '',
        restaurantId: '',
        role: '',
        foodPermitExp: '',
        alcoholPermitExp: ''
    });
    const [attempt, setAttempt] = useState(false);

    const handleSubmit = async (e) => {

        e.preventDefault();
        setAttempt(true);

        const errors = {};

        if (firstName.length > 50) errors.firstName = "First Name can be no more than 50 characters."
        if (lastName.length > 50) errors.lastName = "Last Name can be no more than 50 characters."
        if (restaurantId.length > 10) errors.restaurantId = "Restaurant ID can be no more than 10 characters."

        if (Object.values(errors)[0]) {
            setValidationErrors(errors);
            return alert('Can not submit.');
        }

        setAttempt(false);

        // FIX: dispatch method

    };

    return (
        <div className='employee-form-container'>
            <div className='employee-form-header'>
                <h1>
                    {`${formType} Employee Form`}
                </h1>
            </div>
            <form 
            className='employee-form'
            onSubmit={handleSubmit}
            >
                <div className='employee-form-first-name'>
                    <label>
                        First Name
                    </label>
                    <input 
                        type='text'
                        id='first-name'
                        // placeholder='First Name'
                        value={firstName}
                        onChange={e => setFirstName(e.target.value)}
                    />
                    { attempt && validationErrors.firstName && (<div id='error'>{validationErrors.firstName}</div>) }
                </div>
                <div className='employee-form-last-name'>
                    <label>
                        Last Name
                    </label>
                    <input 
                        type='text'
                        id='last-name'
                        // placeholder='Last Name'
                        value={lastName}
                        onChange={e => setLastName(e.target.value)}
                    />
                    { attempt && validationErrors.lastName && (<div id='error'>{validationErrors.lastName}</div>) }
                </div>
                <div className='employee-form-restaurant-id'>
                    <label>
                        Restaurant ID
                    </label>
                    <input 
                        type='text'
                        id='restaurant-id'
                        // placeholder='Restaurant ID'
                        value={restaurantId}
                        onChange={e => setRestaurantId(e.target.value)}
                    />
                    { attempt && validationErrors.restaurantId && (<div id='error'>{validationErrors.restaurantId}</div>) }
                </div>
                <div className='employee-form-role'>
                    <label>
                        Role (select all that apply)
                    </label>
                </div>
                <div className='employee-form-food-permit-exp'>
                    <label>
                        Food Permit Expiration
                    </label>
                    <input
                        type='date'
                        id='food-permit-exp'
                        value={foodPermitExp}
                        onChange={e => setFoodPermitExp(e.target.value)}
                    />
                </div>
                <div className='employee-form-alcohol-permit-exp'>
                    <label>
                        Alcohol Permit Exipration
                    </label>
                    <input
                        type='date'
                        id='alcohol-permit-exp'
                        value={alcoholPermitExp}
                        onChange={e => setAlcoholPermitExp(e.target.value)}
                    />
                </div>
                <div className='employee-form-action'>
                    <input 
                        className='employee-form-submit-button'
                        type='submit'
                        value = {`${formType} Employee`}
                    />
                </div>
            </form>
        </div>
    );

}