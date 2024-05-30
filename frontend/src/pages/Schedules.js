import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Schedules = () => {
    const [schedules, setSchedules] = useState([]);

    useEffect(() => {
        axios.get('/api/v1/schedules')
            .then(response => setSchedules(response.data))
            .catch(error => console.error('Error fetching schedules:', error));
    }, []);

    return (
        <div>
            <h1>Schedules</h1>
            <ul>
                {schedules.map((schedule, index) => (
                    <li key={index}>{schedule.date}: {schedule.event}</li>
                ))}
            </ul>
        </div>
    );
};

export default Schedules;
