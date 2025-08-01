import { Routes } from '@angular/router';
import { MainViewComponent } from './main-view/main-view.component';
import { GroceryListFormComponent } from './grocery-list-form/grocery-list-form.component';
import { ProductsComponent } from './products/products.component';
import { authGuard } from './auth/auth.guard';

export const routes: Routes = [
  { path: '', component: MainViewComponent },
  { path: 'groceries', component: GroceryListFormComponent, canActivate:[authGuard] },
  { path: 'invite', component: MainViewComponent },
  { path: 'products', component: ProductsComponent, canActivate:[authGuard] },
];
