let result = null;
let itemCount = 10;
const getData =  () => fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
  .then((response) => response.json()); 

async function main() {
  try {
    result = await getData();
	result = result.result.results;
	create();
  } catch(err) {
    console.log(err);
  }
  console.log(result);
}  

function createSmallDom(title,url){
	let smallDiv = document.getElementById("smallCon");
	let smDiv = document.createElement("div");
	smDiv.className = "grid-item";
	let smimg = document.createElement('img');
	smimg.src = url;
	let smSpan = document.createElement("span");
	let smtext = document.createTextNode(title);
	smSpan.className = "smTitle";
	smallDiv.appendChild(smDiv);
	smSpan.appendChild(smtext);
	smDiv.appendChild(smimg);
	smDiv.appendChild(smSpan);
}

function createLargerDom(title,url){
	let row = document.getElementById("largerCon");
	let lgDiv = document.createElement("div");
	lgDiv.className = "grid-item-4";
	let lgimg = document.createElement('img');
	lgimg.src = url;
	let textDiv = document.createElement("div");
	textDiv.className = "titleSty";
	let lgtext = document.createTextNode(title);
	
	row.appendChild(lgDiv);
	textDiv.appendChild(lgtext);
	lgDiv.appendChild(lgimg);
	lgDiv.appendChild(textDiv);
}

function create(){
	for (let i = 0; i < 10; i++){
		let fileUrl = "https://" + result[i].file.split("https://")[1];
		if(i<2) createSmallDom(result[i].stitle, fileUrl);
		else createLargerDom(result[i].stitle, fileUrl);
	}
	const btn = document.createElement("Button");	
	let btntext = document.createTextNode("Load More");
	let btnRow = document.getElementById("loadButton");
	btn.appendChild(btntext);
	btn.className = "btnSty";
	btnRow.appendChild(btn);
	btn.addEventListener("click", function () {
			for (let i = itemCount; i < itemCount+8; i++){
				let fileUrl = "https://" + result[i].file.split("https://")[1];
				createLargerDom(result[i].stitle, fileUrl);
			}
			itemCount = itemCount+8;
			if(itemCount >= result.length)	document.getElementById("loadButton").style.display = "none";
	 });
}

main();