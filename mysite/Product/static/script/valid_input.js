function valid_input(current_amount, event) {
	console.log(current_amount);
	console.log(event.target.value);
	var btnEx = document.getElementById('Export');
	var btnIm = document.getElementById('Import');

	if (current_amount < event.target.value || event.target.value <= 0 || event.target.value == ''){
		btnEx.classList.add('disable');
	}else{
		btnEx.classList.remove('disable');
	}

	if (event.target.value <= 0){
		btnIm.classList.add('disable');
	}else{
		btnIm.classList.remove('disable');
	}

	if (current_amount == 0){
		btnEx.classList.add('disable');
	}
}