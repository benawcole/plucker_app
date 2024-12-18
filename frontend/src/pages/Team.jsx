import React from "react";
import "./Team.css";
import { Navbar } from "../components/Navbar";

export function Team() {
  return (
    <>
    <Navbar />
      <div className="team-container">
        <h1>Meet the team</h1>
        <h3>Ben Cole</h3>
        <h3>Russell Coles</h3>
        <h3>Doug Fairfield</h3>
        <h3>Max Joseph</h3>
        <h3>John O'Neill</h3>
        <h3>Alberto Tobara</h3>
      </div>
    </>
  );
}
