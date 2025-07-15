import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';

export const authGuard: CanActivateFn = (route, state) => {
  const isAuthenticated = !!localStorage.getItem('user'); // Example check
  const router = inject(Router);

  if (!isAuthenticated) {
    router.navigate(['/login']);
    return false;
  }
  return true;
};
