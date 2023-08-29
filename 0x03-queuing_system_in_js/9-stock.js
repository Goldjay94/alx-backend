import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', function () {
  console.log('Redis client connected to the server');
}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById (id) {
  return listProducts.find(item => item.Id === parseInt(id));
}
const get = promisify(client.get).bind(client);

function reserveStockById (itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById (itemId) {
  const stock = await get(itemId);
  return stock;
}

const app = express();
const port = 1245;
app.use(express.json());

app.get('/list_products', (req, res) => {
  const resData = listProducts.map(item => {
    return { itemId: item.Id, itemName: item.name, price: item.price, initialAvailableQuantity: item.stock };
  });
  res.json(resData);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).send({ status: 'Product not found' });
    return;
  }
  const currStock = await getCurrentReservedStockById(itemId);
  res.send({
    itemId: item.Id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: currStock || item.stock
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).send({ status: 'Product not found' });
    return;
  }
  const currStock = await getCurrentReservedStockById(itemId);
  if (currStock && currStock <= 0) {
    res.status(403).send({ status: 'Not enough stock available', itemId: itemId });
    return;
  }
  reserveStockById(itemId, currStock ? currStock - 1 : item.stock - 1);
  res.send({ status: 'Reservation confirmed', itemId: itemId });
});

app.listen(port, () => {});
