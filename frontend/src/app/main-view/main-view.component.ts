import { Component, OnInit } from '@angular/core';
import { GroceryListComponent } from './grocery-list/grocery-list.component';
import { GroceryList } from '../shared/interfaces';
import { GroceryListsService } from '../services/grocery_list.service';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { GroceryListStateService } from '../services/grocery-list-state.service';

@Component({
  selector: 'main-view',
  standalone: true,
  imports: [CommonModule, GroceryListComponent],
  templateUrl: './main-view.component.html',
  styleUrl: './main-view.component.css',
})
export class MainViewComponent implements OnInit {
  groceryLists: GroceryList[] = [];
  constructor(
    private groceryListService: GroceryListsService,
    private groceryListStateService: GroceryListStateService,
    public router: Router
  ) {

  }
  ngOnInit() {
    this.loadGroceryLists();
  }

  loadGroceryLists() {
    this.groceryListService.getGroceryLists().subscribe({
      next: (response) => {
        this.groceryLists = response.data;
      },
      error: (error) => {
        console.error('Error loading grocery lists:', error);
      },
    });
  }
  createNewGroceryList() {
    const user = this.groceryListService.getUser();
    if (!user) {
      console.error('User not found. Cannot create a new grocery list.');
      return;
    }
    this.groceryListStateService.setList(
      {
        name: 'New Grocery List',
        items: [],
        familyId: user.familyId,
        description: '',
      },
      'new'
    );
    this.router.navigate(['/groceries']);
  }

  deleteGroceryList(list: GroceryList) {
    this.groceryListService.deleteGroceryList(list.id as number).subscribe({
      next: (response) => {
        this.groceryLists = this.groceryLists.filter((l) => l.id != list.id);
      },
      error: (error) => {
        console.error('Error loading grocery lists:', error);
      },
    });
  }
}
