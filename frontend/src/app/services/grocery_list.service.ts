import { Injectable } from '@angular/core';
import { ServiceBase } from '../shared/service.base';
import { HttpClient } from '@angular/common/http';
import { GroceryList, GroceryListItem, Message } from '../shared/interfaces';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class GroceryListsService extends ServiceBase {
  constructor(private httpClient: HttpClient) {
    super();
  }

  getGroceryLists(): Observable<Message<GroceryList[]>> {
    const familyId = this.getUser()?.familyId;
    const url = this.buildUrl('groceries', { familyId });
    return this.pipeError(this.httpClient.get(url, this.httpOptions));
  }

  addGroceryList(list: GroceryList): Observable<Message<GroceryList>> {
    const url = this.buildUrl('groceries');
    return this.pipeError(this.httpClient.post(url, list, this.httpOptions));
  }
  updateGroceryList(list: GroceryList): Observable<Message<GroceryList>> {
    const url = this.buildUrl(`groceries/${list.id}`);
    return this.pipeError(this.httpClient.put(url, list, this.httpOptions));
  }
  updateItem(item: GroceryListItem): Observable<Message<GroceryList>> {
    const url = this.buildUrl(`groceries/items/${item.id}`);
    return this.pipeError(this.httpClient.patch(url, item, this.httpOptions));
  }
  deleteGroceryList(listId: number): Observable<Message<GroceryList>> {
    const url = this.buildUrl(`groceries/${listId}`);
    return this.pipeError(this.httpClient.delete(url, this.httpOptions));
  }
}
