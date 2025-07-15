import { Component, OnInit } from '@angular/core';
import { Product } from '../shared/interfaces';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { LookupsService } from '../services/lookups.service';
import { ProductsService } from '../services/products.service';

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './products.component.html',
  styleUrl: './products.component.css',
})
export class ProductsComponent implements OnInit {
  products: Product[] = [];
  constructor(
    private lookupsService: LookupsService,
    private productService: ProductsService
  ) {}
  ngOnInit(): void {
    this.lookupsService.getProducts().subscribe({
      next: (response) => {
        this.products = response.data;
      },
      error: (error) => {
        console.error('Error loading products:', error);
      },
    });
  }

  deleteProduct(productId?: number) {
    if (!productId) {
      return;
    }
    this.productService.deleteProduct(productId).subscribe({
      next: (response) => {
        this.products = this.products.filter((p) => p.id != productId);
      },
      error: (error) => {
        console.error('Error deleting products:', error);
      },
    });
  }
  editProduct(product: Product) {
    this.productForm = product;
  }
  productForm: Product = {
    name: '',
    price: 0,
  };

  onProductSubmit() {
    const user = this.productService.getUser();
    if (this.productForm.id) {
      this.productService.updateProduct(this.productForm).subscribe({
        next: (response) => {
          console.log('Product Updated Succesfully');
        },
        error: (error) => {
          console.error('Error deleting products:', error);
        },
      });
      this.productForm = {
        name: '',
        price: 0,
      };
    } else {
      this.productService.addProduct(this.productForm).subscribe({
        next: (response) => {
          console.log('Product Added Succesfully');
          this.products.push(response.data);
        },
        error: (error) => {
          console.error('Error deleting products:', error);
        },
      });
    }
  }
}
