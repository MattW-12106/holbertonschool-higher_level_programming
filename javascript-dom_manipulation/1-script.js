#!/usr/bin/node
const header = document.querySelector("header")
const redHeader = document.querySelector("#red_header")

/* Event listener for if you click, call function to change colour to red sugoi */
redHeader.addEventListener('click', function () {
  header.style.color = '#FF0000';
});