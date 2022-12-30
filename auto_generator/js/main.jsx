import React from "react";
import { createRoot } from 'react-dom/client'
import Preview from "./tempgenerator";

const root = createRoot(document.getElementById("resumePreview"));
root.render(<Preview/>);