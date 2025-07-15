import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { GroceryList } from '../shared/interfaces';
import { state } from '@angular/animations';

@Injectable({
  providedIn: 'root',
})
export class GroceryListStateService {
  initialGroceryList(): GroceryList {
    return { name: '', items: [], familyId: 0, description: '' };
  }
  private groceryListSubject = new BehaviorSubject<GroceryListState>({
    mode: 'new',
    list: this.initialGroceryList(),
  });
  groceryLists$ = this.groceryListSubject.asObservable();

  setList(list: GroceryList, mode: 'edit' | 'view' | 'new') {
    this.groceryListSubject.next({
      mode,
      list,
    });
  }
  clearList() {
    this.groceryListSubject.next({
      mode: 'new',
      list: this.initialGroceryList(),
    });
  }
}
export type GroceryListState = {
  mode: 'new' | 'edit' | 'view';
  list: GroceryList;
};
