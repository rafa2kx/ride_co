import { TestBed } from '@angular/core/testing';

import { GroceryListStateService } from './grocery-list-state.service';

describe('GroceryListStateService', () => {
  let service: GroceryListStateService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GroceryListStateService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
