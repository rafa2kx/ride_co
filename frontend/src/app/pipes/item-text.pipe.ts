import { Pipe, PipeTransform } from '@angular/core';
import { GroceryListItem } from '../shared/interfaces';

@Pipe({
  name: 'itemText',
  standalone: true,
})
export class ItemTextPipe implements PipeTransform {
  transform(item: GroceryListItem, includeNotes: boolean = false): string {
    return `${item.quantity} ${item.customName || item.product?.name} ${
      includeNotes && item.notes ? `(${item.notes})` : ''
    }`;
  }
}
