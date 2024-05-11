if (!sessionStorage.getItem('welcome_popup_shown')) {
    alert("Hi, welcome to our website!");

    sessionStorage.setItem('welcome_popup_shown', 'true');
}