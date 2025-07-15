import { HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { environment } from '../../environments/environment';
import { AuthService } from '../auth/auth.service';
import { User } from './interfaces';

export class ServiceBase {
  public httpOptions = {
    headers: new HttpHeaders(),
  };
  constructor() {
    try {
      const user = this.getUser();
      this.httpOptions.headers = this.httpOptions.headers.set(
        'Authorization',
        `Bearer ${user?.token}`
      );
    } catch (error) {
      console.error('Error parsing token:', error);
    }
  }

  static handleError(response: any): Observable<never> {
    console.log(response); // eslint-disable-line no-console
    if (response.error.msg === 'Token has expired') {
      localStorage.removeItem('user');
    }
    return throwError(() => response);
  }

  getUser(): User | undefined {
    const json = localStorage.getItem('user');
    return json ? JSON.parse(json) : undefined;
  }

  pipeError(result: Observable<any>) {
    return result.pipe(catchError(ServiceBase.handleError));
  }

  buildUrl(
    path: string,
    query?: Record<string, string | number | null | undefined>
  ): string {
    let host: string = environment.apiUrl;
    if (!host.endsWith('/')) {
      host += '/';
    }
    // Convert query object to query string
    let queryString = '';
    if (query) {
      for (const [key, value] of Object.entries(query)) {
        if (value !== null && value !== undefined) {
          if (queryString) {
            queryString += '&';
          }
          queryString += `${encodeURIComponent(key)}=${encodeURIComponent(
            value
          )}`;
        }
      }
    }
    const url = `${host}${path}${queryString ? `?${queryString}` : ''}`;
    return url.trim();
  }
}
