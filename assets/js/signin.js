// script.js

document.addEventListener("DOMContentLoaded", function() {
    const signInForm = document.getElementById("signin");
    const signUpForm = document.getElementById("signup");

    const signInButton = document.getElementById("signin-button");
    const signUpButton = document.getElementById("signup-button");

    signInButton.addEventListener("click", function() {
        signUpForm.style.display = "none";
        signInForm.style.display = "block";
    });

    signUpButton.addEventListener("click", function() {
        signInForm.style.display = "none";
        signUpForm.style.display = "block";
    });
});