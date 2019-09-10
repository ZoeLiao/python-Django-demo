/**
 * base.js
 * Authors: ZoeLiao
 * Date: 10/09/2019
 * Desc: The script of order/created.html
 * Copyright (c) 2019 ZoeLiao All rights reserved.
 */


addClassNameToForm = () => {
    let ps = $('#orders-form')[0].getElementsByTagName('p');
    for (p of ps){
        p.classList.add('row');
        p.classList.add('my-3');
        let label = p.getElementsByTagName('label')[0];
        if(label){
            label.classList.add('col-5');
        }
        let input = p.getElementsByTagName('input')[0];
        if(input){
            input.classList.add('col-7');
        }
    }
}

$(document).ready(() => {
    addClassNameToForm();
})
