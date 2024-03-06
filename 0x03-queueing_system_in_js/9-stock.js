/**
 * an array of listProducts
 */
import * as redis from 'redis';
const express = require('express');
const app = express();

const listProducts = [
	{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},
	{"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},
	{"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},
	{"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}
];


function getItemById(id){
	for (let item of listProducts){
		if (item.itemId === id){
			return (item);
		}
	}
}

function reserveStockById(itemId, stock){
	const client = redis.createClient();
	client.connect();
	client.set(itemId, stock);
}
reserveStockById(`${listProducts[0].itemId}`, listProducts[0].initialAvailableQuantity);

async function getCurrentReservedStockById(itemId){
	const client = redis.createClient();
	client.connect();
	return (client.get(itemId));
};

// api definition
app.get('/list_products/:itemId?', async (req, res) =>{
	let itemId = req.params.itemId;
	if (itemId){
		//itemId = parseInt(itemId);
		const item = await getCurrentReservedStockById(itemId);
		if (!item){
			res.send({'status':'Product not found'});
		}else{
			res.send(
				{
					...(getItemById(parseInt(itemId))), 
					currentQuantity: item
				});
		}
	}else{
		res.send(listProducts);
	}
});

app.get('/reserve_product/:itemId', async (req, res) =>{
	let itemId = req.params.itemId;
	//itemId = parseInt(itemId);
	
	const item = await getCurrentReservedStockById(itemId);
	if (!item){
		res.send({'status':'Product not found'});
	}else if(item < 1){
		res.send({
			'status':'Not enough stock available',
			'itemId': parseInt(itemId)
		});
	}else{
		res.send({
			"status":"Reservation confirmed",
			"itemId": parseInt(itemId)
		});
	}
});


app.listen(1245, () => {
	console.log(`Server is running on http://localhost:1245`);
	}
);
