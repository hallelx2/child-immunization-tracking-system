import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Profile from './pages/Profile';
import Immunizations from './pages/Immunizations';
import Milestones from './pages/Milestones';
import Schedules from './pages/Schedules';
import Reports from './pages/Reports';

const App = () => {
    return (
        <Router>
            <Navbar />
            <Switch>
                <Route path="/" exact component={Home} />
                <Route path="/profile" component={Profile} />
                <Route path="/immunizations" component={Immunizations} />
                <Route path="/milestones" component={Milestones} />
                <Route path="/schedules" component={Schedules} />
                <Route path="/reports" component={Reports} />
            </Switch>
        </Router>
    );
};

export default App;
