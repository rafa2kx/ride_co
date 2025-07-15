export interface Message<T> {
  data: T;
  message: string;
  success: boolean;
}
export interface User {
  id?: number;
  username: string;
  email: string;
  familyId: number;
  familyName?: string;
  picture?: string;
  token?: string;
}

export interface GroceryList {
  createdAt?: Date;
  createdBy?: string;
  description: string;
  familyId: number;
  id?: number;
  items: GroceryListItem[];
  name: string;
  updatedAt?: Date;
  updatedBy?: string;
}

export interface GroceryListItem {
  createdAt?: Date;
  createdBy?: string;
  customName?: string;
  groceryListId?: number;
  id?: number;
  notes?: string;
  productId?: number;
  purchased: boolean;
  quantity: number;
  updatedAt?: Date;
  updatedBy?: string;
  product?: Product;
}
export interface Product {
  // categoryId: number;
  // createdAt: Date;
  // createdBy: string;
  description?: string;
  id?: number;
  name: string;
  price: number;
  // updatedAt: Date;
  // updatedBy: string;
}
