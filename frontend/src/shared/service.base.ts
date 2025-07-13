import { HttpHeaders } from "@angular/common/http";
import { Observable, throwError } from "rxjs";
import { catchError } from "rxjs/operators";
import { formatDate } from '@angular/common';

export class ServiceBase {

  public httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  static handleError(error: any) {
    console.log(error); // eslint-disable-line no-console
    return throwError(() => error);
  }

  pipeError(result: Observable<any>) {
    return result.pipe(catchError(ServiceBase.handleError));
  }
}