import { Injectable } from '@angular/core';
import { ServiceBase } from '../shared/service.base';
import { Message, Product } from '../shared/interfaces';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ProductsService extends ServiceBase {
  constructor(private httpClient: HttpClient) {
    super();
  }
  addProduct(product: Product): Observable<Message<Product>> {
    const familyId = this.getUser()?.familyId;
    const url = this.buildUrl('products', { familyId });
    return this.pipeError(this.httpClient.post(url, product, this.httpOptions));
  }
  updateProduct(product: Product): Observable<Message<Product>> {
    const url = this.buildUrl(`products/${product.id}`);
    return this.pipeError(this.httpClient.put(url, product, this.httpOptions));
  }
  deleteProduct(productId: number): Observable<Message<Product[]>> {
    const url = this.buildUrl(`products/${productId}`);
    return this.pipeError(this.httpClient.delete(url, this.httpOptions));
  }
}
