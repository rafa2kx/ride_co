import { TestBed } from '@angular/core/testing';

import { GroceryListsService } from './grocery_list.service';

describe('GroceryListsService', () => {
  let service: GroceryListsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GroceryListsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
