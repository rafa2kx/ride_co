import { Component, Input, OnInit } from '@angular/core';
import {
  GroceryList,
  GroceryListItem,
  Product,
  User,
} from '../shared/interfaces';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { GroceryListStateService } from '../services/grocery-list-state.service';
import { LookupsService } from '../services/lookups.service';
import { GroceryListsService } from '../services/grocery_list.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-grocery-list-form',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './grocery-list-form.component.html',
  styleUrl: './grocery-list-form.component.css',
})
export class GroceryListFormComponent implements OnInit {
  showDescription = false;
  products: Product[] = [];
  mode: 'new' | 'edit' | 'view' = 'new';
  model: GroceryList = {
    id: 0,
    name: '',
    items: [],
    familyId: 0,
    description: '',
  };

  ngOnInit(): void {
    this.lookupsService.getProducts().subscribe({
      next: (response) => {
        this.products = response.data;
      },
      error: (error) => {
        console.error('Error loading products:', error);
      },
    });
    this.model.familyId = this.lookupsService.getUser()?.familyId || 0;
  }

  constructor(
    private groceryListState: GroceryListStateService,
    private groceryListService: GroceryListsService,
    private lookupsService: LookupsService,
    private router: Router
  ) {
    this.groceryListState.groceryLists$.subscribe((state) => {
      this.model = state.list;
      console.log('Grocery list state:', this.model);
      this.mode = state.mode;
    });
  }

  handleProductChange(item: GroceryListItem) {
    if (item.productId) {
      const product = this.products.find((p) => p.id == item.productId);
      if (product) {
        item.customName = product.name;
      }
    }
  }

  addItem() {
    this.model.items.push({
      customName: '',
      quantity: 1,
      groceryListId: this.model.id,
      notes: '',
      purchased: false,
    });
  }

  handleItemPurchased(item: GroceryListItem) {
    if (item.purchased) {
      item.updatedAt = new Date();
      item.updatedBy = this.lookupsService.getUser()?.username || '';
    } else {
      item.updatedAt = undefined;
      item.updatedBy = undefined;
    }

    this.groceryListService.updateItem(item).subscribe({
      next: (response) => {
        console.log('Item updated successfully:', response);
      },
      error: (error) => {
        console.error('Error updating item:', error);
      },
    });
  }

  removeItem(index: number) {
    this.model.items.splice(index, 1);
  }

  saveGroceryList() {
    if (this.mode === 'new') {
      this.groceryListService.addGroceryList(this.model).subscribe({
        next: (response: any) => {
          console.log('Grocery list added successfully:', response);
          this.groceryListState.clearList();
          this.router.navigate(['/']);
        },
        error: (error: any) => {
          console.error('Error adding grocery list:', error);
        },
      });
    } else if (this.mode === 'edit') {
      this.groceryListService.updateGroceryList(this.model).subscribe({
        next: (response: any) => {
          console.log('Grocery list updated successfully:', response);
          this.groceryListState.clearList();
          this.router.navigate(['/']);
        },
        error: (error: any) => {
          console.error('Error updating grocery list:', error);
        },
      });
    }
  }
}
