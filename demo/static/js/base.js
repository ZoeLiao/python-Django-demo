/**
 * base.js
 * Authors: ZoeLiao
 * Date: 10/09/2019
 * Desc: The base script of base.html
 * Copyright (c) 2019 ZoeLiao All rights reserved.
 */


changeNavColor = () => {
    let navbar = $('#base-navbar')[0];
    if (window.scrollY > 100) {
        navbar.classList.add('navbar-suspend-white')
    } else {
        if (navbar.classList.contains('navbar-suspend-white')) {
            navbar.classList.remove('navbar-suspend-white')
        }
    }
}

$(window).scroll(() => {
    changeNavColor()
})
