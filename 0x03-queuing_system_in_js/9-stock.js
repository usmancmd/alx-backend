import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const app = express()
const client = createClient()

const listProducts = [
  {
    Id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    Id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    Id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    Id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
]

const getItemById = (id) => {
  const item = listProducts.find((product) => id === product.id)
  if (item) {
    return Object.fromEntries(Object.entries(item));
  }
}

const reserveStockById = (itemId, stock) => {
  return promisify(client.SET).bind(client)(`item.${itemId}`, stock);
}

const getCurrentReservedStockById = async (itemId) => {
  return promisify(client.GET).bind(client)(`item.${itemId}`);
}


app.get('/list_products', (req, res) => {
  res.json(listProducts);
})

app.get('/list_products/:itemId', (req, res) => {
  const itemId = Number(req.params.itemId)
  const productItem = getItemById(Number(itemId));
  if (!productItem) {
     return res.send({"status":"Product not found"})
  }
  res.send(getCurrentReservedStockById(itemId))
})

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = Number(req.params.itemId);
  const productItem = getItemById(Number(itemId));

  if (!productItem) {
    return res.json({ status: 'Product not found' });
  }
  getCurrentReservedStockById(itemId)
    .then((result) => Number(result || 0))
    .then((reservedStock) => {
      if (reservedStock >= productItem.initialAvailableQuantity) {
        res.json({ status: 'Not enough stock available', itemId });
        return;
      }
      reserveStockById(itemId, reservedStock + 1)
        .then(() => {
          res.json({ status: 'Reservation confirmed', itemId });
        });
    });
})

app.listen(1245, () => console.log("server listen on port 1245"))
