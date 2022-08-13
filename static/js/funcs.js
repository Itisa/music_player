function lower_bound(arr,num) {
	let l = 0,r = arr.length - 1;
	let i = 0;
	while (true) {
		i += 1;if (i >= 100){console.log("lower_bound error",arr,num); return -1;}
		let mid = Math.floor( (l+r)/2 );
		if (l == mid){
			if (num > arr[r]){return r;}
			else{return l;}
		}
		if (arr[mid] - num < 1e-13) {l = mid;}
		else {r = mid;}
		if (l == r){return l;}
	}
}