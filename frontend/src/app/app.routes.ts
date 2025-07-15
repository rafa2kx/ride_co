import { Routes } from '@angular/router';
import { MainViewComponent } from './main-view/main-view.component';
import { GroceryListFormComponent } from './grocery-list-form/grocery-list-form.component';

export const routes: Routes = [
  { path: '', component: MainViewComponent },
  { path: 'groceries', component: GroceryListFormComponent },
  { path: 'invite', component: MainViewComponent },
];
