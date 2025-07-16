import { Injectable } from '@angular/core';
import { ServiceBase } from '../shared/service.base';
import { HttpClient } from '@angular/common/http';
import { Message, Product } from '../shared/interfaces';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LookupsService extends ServiceBase {
  constructor(private httpClient: HttpClient) {
    super();
  }
  getProducts(): Observable<Message<Product[]>> {
    const familyId = this.getUser()?.familyId;
    const url = this.buildUrl('products', { familyId });
    return this.pipeError(this.httpClient.get(url, this.httpOptions));
  }
}
