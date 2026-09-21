import React from 'react';
import {createRoot} from 'react-dom/client';
import Hub from '../hub/Hub';
import '../app/globals.css';
import './pages.css';

createRoot(document.getElementById('root')!).render(<React.StrictMode><Hub/></React.StrictMode>);
