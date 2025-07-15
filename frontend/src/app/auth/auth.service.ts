import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ServiceBase } from '../shared/service.base';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { Message, User } from '../shared/interfaces';

@Injectable({
  providedIn: 'root',
})
export class AuthService extends ServiceBase {
  constructor(private httpClient: HttpClient) {
    super();
  }
  setUser(user: User): void {
    localStorage.setItem('user', JSON.stringify(user));
  }

  authenticate(token: string, familyId?: number): Observable<Message<User>> {
    const url = this.buildUrl('auth'); //`${environment.apiUrl}/auth`; // Replace with your backend URL
    return this.pipeError(
      this.httpClient.post(url, { token, familyId }, this.httpOptions)
    );
  }
}
