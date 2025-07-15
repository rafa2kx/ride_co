import { Component, EventEmitter, Input, Output } from '@angular/core';
import { GroceryList } from '../../shared/interfaces';
import { CommonModule } from '@angular/common';
import { ItemTextPipe } from '../../pipes/item-text.pipe';
import { GroceryListStateService } from '../../services/grocery-list-state.service';
import { Router } from '@angular/router';

@Component({
  selector: 'grocery-list',
  standalone: true,
  imports: [CommonModule, ItemTextPipe],
  templateUrl: './grocery-list.component.html',
  styleUrl: './grocery-list.component.css',
})
export class GroceryListComponent {
  @Input() groceryList?: GroceryList;
  @Output() deleteGroceryListEvent = new EventEmitter<GroceryList>();
  constructor(
    public groceryListStateService: GroceryListStateService,
    private router: Router
  ) {}

  showGroceryList(mode: 'edit' | 'view') {
    this.groceryListStateService.setList(this.groceryList as GroceryList, mode);
    this.router.navigate(['/groceries']);
  }
  deleteGroceryList(event:Event) {
    event.stopPropagation();
    this.deleteGroceryListEvent.emit(this.groceryList);
  }
}
