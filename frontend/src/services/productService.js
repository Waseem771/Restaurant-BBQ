// src/services/productService.js
import { apiRequest } from '../lib/api';

export async function addProduct(product) {
  return apiRequest('/v1/products/', {
    method: 'POST',
    body: JSON.stringify(product),
  });
}

export async function getAllProducts() {
  return apiRequest('/v1/products/');
}
